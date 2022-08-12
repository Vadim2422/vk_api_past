from fastapi import APIRouter
router = APIRouter(tags=['get'])

@router.get("/")
def home():
  return "Монитор активен"