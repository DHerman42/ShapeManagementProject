function customerFilter() {
	let customerInput = document.getElementById("customerFilter").value.toUpperCase();
	let jobInput = document.getElementById("jobFilter").value.toUpperCase();
	let table = document.getElementById("shapeTable");
	let tr = table.getElementsByTagName("tr");

	for (let i = 0; i < tr.length; i++) {
		let customerData = tr[i].getElementsByTagName("td")[2];
		if (customerData) {
			customerValue = customerData.textContent || customerData.innerText;
			if (customerValue.toUpperCase().indexOf(customerInput) > -1) {
				tr[i].style.display = "";
			} else {
				tr[i].style.display = "none";
			}
		}
	}
}

function jobFilter(){
    let customerInput = document.getElementById("customerFilter").value.toUpperCase();
	let jobInput = document.getElementById("jobFilter").value.toUpperCase();
	let table = document.getElementById("shapeTable");
	let tr = table.getElementsByTagName("tr");

    for (let i = 0; i < tr.length; i++) {
        let jobData = tr[i].getElementsByTagName("td")[3];
        if (jobData) {
            jobValue = jobData.textContent || jobData.innerText;
            if (jobValue.toUpperCase().indexOf(jobInput) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function clearFilter(){
    document.getElementById("customerFilter").value = "";
	document.getElementById("jobFilter").value = "";

    let table = document.getElementById("shapeTable");
	let tr = table.getElementsByTagName("tr");

    for(let i = 0; i < tr.length; i++){
        tr[i].style.display = "";
    }
}