import asyncio
from aijson import Flow
from dotenv import load_dotenv

load_dotenv()

async def main():
    # Get user input
    income = float(input("Enter your monthly income: "))
    expenses = {}
    while True:
        category = input("Enter expense category (or 'done' to finish): ")
        if category.lower() == 'done':
            break
        amount = float(input(f"Enter amount for {category}: "))
        expenses[category] = amount
    
    savings_goal = float(input("Enter your monthly savings goal: "))
    
    # Create and run the flow
    flow = Flow.from_file('flow.ai.yaml')
    flow = flow.set_vars(
        income=income,
        expenses=expenses,
        savings_goal=savings_goal,
        total_expenses=sum(expenses.values())
    )
    
    results = await flow.run()
    
    # Print results
    print("\nFinancial Report:")
    print(results)

if __name__ == "__main__":
    asyncio.run(main())