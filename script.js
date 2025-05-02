// script.js
fetch('https://expensestreamline-backend.onrender.com/add-expense', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ item: "Coffee", amount: 50 })
})
.then(res => res.json())
.then(data => console.log(data));
