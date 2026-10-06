#!/usr/bin/env python3
"""SDK의 실제 도구 목록과 알려진 조회·변경 경계를 검사한다. 원격 도구는 호출하지 않는다."""
import argparse
import asyncio
import importlib
import json


async def check(server: str) -> int:
    module = importlib.import_module(server.replace("-", "_") + ".server")
    tools = {t.name: t for t in await module.mcp.list_tools()}
    errors = []
    for name, tool in tools.items():
        a = tool.annotations
        if a is None or any(type(getattr(a, key)) is not bool for key in
                            ("readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint")):
            errors.append(f"{name}: 네 동작 힌트의 boolean 값이 필요합니다")
        elif a.readOnlyHint and (a.destructiveHint or not a.idempotentHint):
            errors.append(f"{name}: 읽기와 변경 힌트가 모순됩니다")
    # 서로 다른 HTTP 메서드·로컬 작업·혼합 action을 대표하는 회귀 사례.
    boundaries = {
        "moai-mcp-ip": {"ip_check_access": (True, False, True, True)},
        "moai-mcp-openai": {"openai_image_generate": (False, False, False, True)},
        "moai-mcp-smartstore": {"smartstore_config_status": (True, False, True, False),
                               "sku_list": (True, False, True, True),
                               "product_search": (True, False, True, True),
                               "order_query_product_orders": (True, False, True, True),
                               "order_dispatch": (False, True, False, True)},
        "moai-mcp-threads-poster": {"threads_style_save": (False, True, True, False),
                                  "threads_format_multi_channel": (True, False, True, False),
                                  "instagram_comments_hide": (False, True, False, True)},
        "moai-mcp-imweb": {"imweb_product": (False, True, False, True)},
        "moai-mcp-cafe24": {"cafe24_product": (False, True, False, True),
                           "cafe24_analytics": (True, False, True, True)},
    }
    for name, expected in boundaries[server].items():
        a = tools[name].annotations if name in tools else None
        actual = tuple(getattr(a, k, None) for k in
                       ("readOnlyHint", "destructiveHint", "idempotentHint", "openWorldHint"))
        if actual != expected:
            errors.append(f"{name}: 경계 사례 불일치 {actual} != {expected}")
    print(json.dumps({"server": server, "registered_tools": len(tools), "errors": errors,
                      "remote_operations_invoked": 0}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--server", required=True)
    args = parser.parse_args()
    raise SystemExit(asyncio.run(check(args.server)))
