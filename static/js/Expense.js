var selectedRow = null;

function onFormSubmit() {

    var formData = readFormData();
    if (selectedRow == null) {
        
    } else {
        updateRecord(formData);
    }
    
}


//Retrieve the data
function readFormData() {
    var formData = {};
    formData["productCode"] = document.getElementById("productCode").value;
    formData["product"] = document.getElementById("product").value;
    formData["qty"] = document.getElementById("qty").value;
    formData["perPrice"] = document.getElementById("perPrice").value;
    return formData;
}



function insertNewRecord(data) {
    console.log('hello man');
    var table = document.getElementById("storeList").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    
    // Set the data-expense-id attribute with a unique value (you may need to adjust this based on your actual data)
    newRow.setAttribute("data-expense-id", "newExpense" + Math.random().toString(36).substring(7));

    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.productCode;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.product;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.qty;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.perPrice;
    cell4 = newRow.insertCell(4);
    cell4.innerHTML = `<button onClick="onEdit(this)">Edit</button> <button onClick="onDelete(this)">Delete</button>`;
}

function formatDate(date) {

    var dateFromTableCell = selectedRow.cells[2].innerHTML;

    var parsedDate = new Date(dateFromTableCell);

    var year = parsedDate.getFullYear();
    var month = ('0' + (parsedDate.getMonth() + 1)).slice(-2); // Adding 1 because months are zero-indexed
    var day = ('0' + parsedDate.getDate()).slice(-2);

    var formattedDate = year + '-' + month + '-' + day;
    return formattedDate;

}

function onEdit(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("productCode").value = selectedRow.cells[0].innerHTML;
    document.getElementById("product").value = selectedRow.cells[1].innerHTML;
    document.getElementById("qty").value = formatDate(selectedRow.cells[2].innerHTML);
    document.getElementById("perPrice").value = selectedRow.cells[3].innerHTML;
}

//Reset the data
function resetForm() {
    document.getElementById("productCode").value = '';
    document.getElementById("product").value = '';
    document.getElementById("qty").value = '';
    document.getElementById("perPrice").value = '';
    selectedRow = null;
}


// Update record
function updateRecord(formData) {
    $.ajax({
        type: 'POST',
        url: `edit_expense/${selectedRow.dataset.expenseId}/`,
        data: {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
            productCode: formData.productCode,
            product: formData.product,
            qty: formData.qty,
            perPrice: formData.perPrice
        },
        success: function(response) {
            console.log(response);  // Log the response for debugging
            if (response.status === 'success') {
                selectedRow.cells[0].innerHTML = formData.productCode;
                selectedRow.cells[1].innerHTML = formData.product;
                selectedRow.cells[2].innerHTML = formData.qty;
                selectedRow.cells[3].innerHTML = formData.perPrice;
            } else {
                alert('Failed to update expense. Please try again.');
            }
        },
        error: function(xhr, status, error) {
            console.error(error);  // Log the error for debugging
            alert('Failed to update expense. Please try again.');
        }
    });
}

// Delete record
function onDelete(td) {
    if (confirm('Do you want to delete this record?')) {
        row = td.parentElement.parentElement;
        $.ajax({
            type: 'POST',
            url: `delete_expense/${row.dataset.expenseId}/`,
            data: {
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
            },
            success: function(response) {
                console.log(response);  // Log the response for debugging
                if (response.status === 'success') {
                    document.getElementById('storeList').deleteRow(row.rowIndex);
                    resetForm();
                } else {
                    alert('Failed to delete expense. Please try again.');
                }
            },
            error: function(xhr, status, error) {
                console.error(error);  // Log the error for debugging
                alert('Failed to delete expense. Please try again.');
            }
        });
    }
}
