# Path: app/bingx/bingx.py
# Description: Routes for BingX exchange

from fastapi import APIRouter

from app.bingx.routes import coinm, main, spot, usdtm, standard

router = APIRouter()

router.include_router(coinm.router, prefix="/coinm", tags=["coinm"])
router.include_router(main.router, prefix="/main", tags=["main"])
router.include_router(spot.router, prefix="/spot", tags=["spot"])
router.include_router(usdtm.router, prefix="/usdtm", tags=["usdtm"])
router.include_router(standard.router, prefix="/standard", tags=["standard"])
    
    

    
