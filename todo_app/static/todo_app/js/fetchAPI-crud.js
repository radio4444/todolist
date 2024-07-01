document.addEventListener('DOMContentLoaded', function (){
    // Select the container where the table will be placed
    const container = document.getElementById('todolist-container')

    const table = document.createElement('table')

    const headerRow = document.createElement('tr')

    const headers = ['Task Name', 'Description', 'Priority' , 'Deadline' ,'Status'
        , 'Created', 'Edited']

    // Add the head cell
    headers.forEach(header => {
        const th = document.createElement('th')
        th.textContent = header
        headerRow.append(th)
    })

    // Append the headerRow to the table
    table.append(headerRow)

    // Append the table to container
    container.append(table)
})