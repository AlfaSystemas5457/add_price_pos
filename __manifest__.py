{
    "name": "Add price to POS product card",
    "summary": "Add price info to POS product card",
    "description": """Add price info to POS product card""",
    "author": "DGV",
    # 'website': "https://www.yourcompany.com",
    "category": "Point of Sale",
    "version": "0.1",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale._assets_pos": [
            "add_price_pos/static/src/**/*",
        ],
    },
}
