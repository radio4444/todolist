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

    const dummyDataArray2 = ['No task2', 'No Description2', 'No Priority2',
        'No Deadline2', 'No Status2', 'No Created2', 'No Edited2'];

    const rowData1 = document.createElement('tr');

    // Add the dummyData in the cell
    dummyDataArray.forEach(dummyData => {
        const td = document.createElement('td');
        td.textContent = dummyData;
        rowData1.append(td);
    });

    const rowData2 = document.createElement('tr');
    dummyDataArray2.forEach(dummyData => {
        const td = document.createElement('td');
        td.textContent = dummyData;
        rowData2.append(td);
    });

    table.append(rowData1);
    table.append(rowData2);


    // Append the table to container
    container.append(table);
});