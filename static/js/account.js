const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

// Function to calculate and update the total balance for a member
function updateTotalBalance(memberRow) {
    let total = 0;
    const amountInputs = memberRow.querySelectorAll('.amount');
    const totalCell = memberRow.querySelector('.total');

    for (let i = 0; i < amountInputs.length; i++) {
        total += parseFloat(amountInputs[i].value) || 0;
    }

    totalCell.textContent = total;
}

// Function to add a new member row to the table
function addMemberRow(memberName) {
    const paymentTable = document.getElementById('paymentTable');
    const newRow = document.createElement('tr');
    newRow.innerHTML = `<td>${memberName}</td>`;
    for (let month of months) {
        newRow.innerHTML += `<td><input class="amount" type="number" value="0"></td>`;
    }
    newRow.innerHTML += `<td class="total"></td>`;
    paymentTable.appendChild(newRow);

    const amountInputs = newRow.querySelectorAll('.amount');
    for (let input of amountInputs) {
        input.addEventListener('input', () => {
            updateTotalBalance(newRow);
        });
    }
}

const members = [
    'Shahjahan', 'Kader-1','Kader-2', 'Rony', 'Mahibul', 'Shahalom','Yousuf','Jamal-1','Jamal-2', 'Topu', 'Nizam', 'Tamjid-1','Tamjid-2','Tawsif', 'Mizan',
    'Sayed', 'Al-amin','Rafe'];

members.forEach(member => addMemberRow(member));
