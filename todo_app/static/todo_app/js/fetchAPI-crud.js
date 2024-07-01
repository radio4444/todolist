document.addEventListener('DOMContentLoaded', function () {
    // Select the container where the table will be placed
    const container = document.getElementById('todolist-container');

    const table = document.createElement('table');

    const headerRow = document.createElement('tr');

    const headers = ['Task Name', 'Description', 'Priority', 'Deadline',
        'Status', 'Created', 'Edited'];

    // Add the head cell
    headers.forEach(header => {
        const th = document.createElement('th');
        th.textContent = header;
        headerRow.append(th);
    });

    // Append the headerRow to the table
    table.append(headerRow);

    // Create dummyData for the table
    const dummyDataArray = ['No task', 'No Description', 'No Priority',
        'No Deadline', 'No Status', 'No Created', 'No Edited'];


    const rowData1 = document.createElement('tr');

    // Add the dummyData in the cell
    dummyDataArray.forEach(dummyData => {
        const td = document.createElement('td');
        td.textContent = dummyData;
        rowData1.append(td);
    });


    table.append(rowData1);

    // Django Rest endpoint
    const endpoint = '/api/tasks/';

    // fetch the data using Django REST API
    fetch(endpoint)
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Request Failed');

        }, networkError => console.log(networkError.message))
        .then(data => {
            console.table(data);

            data.forEach(item => {
                const rowData = document.createElement('tr');

                const keys = Object.keys(item);
                // Loop through each property of the object, except id

                keys.forEach(key => {
                    if (key !== 'id') {
                        const td = document.createElement('td');
                        td.textContent = item[key]
                        rowData.append(td);
                    }
                });

                table.append(rowData);
            });


        });


    // Append the table to container
    container.append(table);
});

