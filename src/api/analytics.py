from fastapi import APIRouter

router = APIRouter()


@router.get("/analytics")
def analytics():

    return {

        "average_sales": 52.42,

        "total_sales": 913000,

        "max_sales": 231,

        "min_sales": 0,

        "monthly_sales": [

            {"month": "Jan", "sales": 1200},
            {"month": "Feb", "sales": 1400},
            {"month": "Mar", "sales": 1500},
            {"month": "Apr", "sales": 1700},
            {"month": "May", "sales": 1850},
            {"month": "Jun", "sales": 1950},
            {"month": "Jul", "sales": 2050},
            {"month": "Aug", "sales": 1980},
            {"month": "Sep", "sales": 1800},
            {"month": "Oct", "sales": 1750},
            {"month": "Nov", "sales": 1900},
            {"month": "Dec", "sales": 2200},
        ],

        "weekly_sales": [

            {"week": "W1", "sales": 210},
            {"week": "W2", "sales": 225},
            {"week": "W3", "sales": 240},
            {"week": "W4", "sales": 260},
            {"week": "W5", "sales": 280},
            {"week": "W6", "sales": 300},
            {"week": "W7", "sales": 320},
            {"week": "W8", "sales": 330},
        ],

        "store_sales": [

            {"store": "Store 1", "sales": 8200},
            {"store": "Store 2", "sales": 7600},
            {"store": "Store 3", "sales": 9100},
            {"store": "Store 4", "sales": 6400},
            {"store": "Store 5", "sales": 8700},
        ],

        "item_sales": [

            {"item": "Item 1", "sales": 9200},
            {"item": "Item 2", "sales": 8800},
            {"item": "Item 3", "sales": 8200},
            {"item": "Item 4", "sales": 7600},
            {"item": "Item 5", "sales": 7200},
        ],

        "heatmap": [

            {"date": "2017-01-01", "count": 10},
            {"date": "2017-01-02", "count": 20},
            {"date": "2017-01-03", "count": 40},
            {"date": "2017-01-04", "count": 70},
            {"date": "2017-01-05", "count": 90},
        ],
    }
