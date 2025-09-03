from fastapi import APIRouter
from pydantic import BaseModel
import crew.utils as utils


plan_router = APIRouter(
    prefix='/api/v1/account',
    tags=['api_v1', 'account']
)

class UpdatePlan(BaseModel):
    customer_id: str
    subscription_plan: str

@plan_router.post("/update-plan")
async def update_plan(new_plan: UpdatePlan):
    utils.add_or_update_subscription(
        new_plan.customer_id,
        new_plan.subscription_plan
    )
    return {
        "message": "Plan Updated Successfully"
    }

@plan_router.get("/get-plan")
async def get_plan(customer_id: str):
    response = utils.get_subscription(
        customer_id
    )
    return {
        "message": response
    }