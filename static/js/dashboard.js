document.addEventListener('DOMContentLoaded', function() {
    // Sample data - replace with real data from your backend
    const financialData = {
        income: 5000,
        expenses: 3500,
        savings: 1500
    };

    // Update summary cards
    document.getElementById('total-income').textContent = `$${financialData.income}`;
    document.getElementById('total-expenses').textContent = `$${financialData.expenses}`;
    document.getElementById('net-savings').textContent = `$${financialData.savings}`;

    // Create Income vs Expense chart
    Highcharts.chart('income-expense-chart', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Income vs Expenses'
        },
        xAxis: {
            categories: ['January', 'February', 'March', 'April', 'May']
        },
        yAxis: {
            title: {
                text: 'Amount ($)'
            }
        },
        series: [{
            name: 'Income',
            data: [4500, 5000, 4800, 5200, 5000]
        }, {
            name: 'Expenses',
            data: [3200, 3500, 3300, 3700, 3500]
        }]
    });

    // Create Savings Goal chart
    Highcharts.chart('savings-goal-chart', {
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Savings Goals Progress'
        },
        series: [{
            name: 'Amount',
            data: [
                { name: 'Emergency Fund', y: 2000 },
                { name: 'Vacation', y: 1000 },
                { name: 'New Laptop', y: 500 }
            ]
        }]
    });

    // Populate recent transactions
    const transactions = [
        { date: '2023-08-01', description: 'Salary', amount: 5000, type: 'income' },
        { date: '2023-08-02', description: 'Rent', amount: -1500, type: 'expense' },
        { date: '2023-08-03', description: 'Groceries', amount: -200, type: 'expense' }
    ];

    const transactionTable = document.getElementById('transactions-table');
    transactions.forEach(transaction => {
        const row = transactionTable.insertRow();
        row.insertCell(0).textContent = transaction.date;
        row.insertCell(1).textContent = transaction.description;
        row.insertCell(2).textContent = `$${Math.abs(transaction.amount)}`;
        row.insertCell(3).textContent = transaction.type;
    });
});