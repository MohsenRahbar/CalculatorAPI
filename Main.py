from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import math


app = FastAPI()

class Calculation(BaseModel):
    num1: float
    num2: float
    operation: str

@app.post("/calculate")
async def calculate(calculation: Calculation):
    num1 = calculation.num1
    num2 = calculation.num2
    operation = calculation.operation.lower()

    if operation == "sum":
        result = num1 + num2
    elif operation == "product":
        result = num1 * num2
    elif operation == "difference":
        result = num1 - num2
    elif operation == "division":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        result = num1 / num2
    elif operation == "sqrt":
        if num1 < 0:
            raise HTTPException(status_code=400, detail="Cannot calculate square root of a negative number")
        result = num1**0.5
    elif operation == "log":
        if num1 <= 0:
            raise HTTPException(status_code=400, detail="Cannot calculate log of a non-positive number")
        result= math.log(num1)
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return {"result": result}
