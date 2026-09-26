"""FastMCP application instance — single shared `mcp` object.

Tools are registered dynamically from the declarative endpoint registry by
:mod:`moai_mcp_cafe24.tools._dispatch`. :mod:`moai_mcp_cafe24.server` imports the tool
modules to populate the registry, then runs the server.

Keeping the instance in its own module avoids a circular import between
``server`` (runs the server) and ``tools.*`` (populate the registry).
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

# Server instructions guide tool-search discovery for the 20 category tools.
# Kept under the 2KB truncation ceiling; the README holds the full surface map.
_INSTRUCTIONS = (
    "Cafe24 shopping-mall operations, management, and analytics — Admin API "
    "(19 domains: product, order, store, customer, promotion, design, category, "
    "collection, supply, shipping, mileage, community, notification, translation, "
    "personal, privacy, salesreport, application, analytics_admin) plus Analytics "
    "API / cafe24data (visitors, sales, ads, keywords, traffic-source stats). "
    "Use these tools whenever the user asks about a Cafe24 mall: products, orders, "
    "customers, store/app settings, promotions, design, shipping, mileage, or any "
    "traffic/sales analytics. Tool names follow the pattern "
    "'cafe24_<domain>' (e.g. cafe24_product, cafe24_order, cafe24_analytics). "
    "Choose the action enum for the operation and pass path/query values in params. "
    "Write operations accept a body dictionary. List actions accept "
    "'paginate' + 'max_pages' for transparent offset paging. The 'shop_no' "
    "parameter selects a multi-shop number (defaults per config)."
)

mcp: FastMCP = FastMCP("moai-mcp-cafe24", instructions=_INSTRUCTIONS)
