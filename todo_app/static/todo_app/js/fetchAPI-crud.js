document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('todolist-container');
    const table = document.createElement('table');
    const headerRow = document.createElement('tr');
    const headers = ['Task Name', 'Description', 'Priority', 'Deadline',
        'Status', 'Created', 'Edited', 'Delete', 'Update'];

    headers.forEach(header => {
        const th = document.createElement('th');
        th.textContent = header;
        headerRow.append(th);
    });

    table.append(headerRow);
    container.append(table);

    const endpoint = '/api/tasks/';

    fetchTasks();

    function fetchTasks() {
        fetch(endpoint)
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Request Failed');
            })
            .then(data => {
                data.forEach(item => {
                    appendTaskToTable(item);
                });
            })
            .catch(error => console.log(error.message));
    }

    const createTaskButton = document.getElementById('create-task-button');
    const createTaskFormContainer = document.getElementById('create-task-form-container');
    const createTaskForm = document.getElementById('create-task-form');
    const updateTaskFormContainer = document.getElementById('update-task-form-container');
    const updateTaskForm = document.getElementById('update-task-form');

    createTaskButton.addEventListener('click', () => {
        createTaskFormContainer.style.display = 'block';
    });

    createTaskForm.addEventListener('submit', event => {
        event.preventDefault();

        const formData = new FormData(createTaskForm);
        const task_detail_data = {
            task_name: formData.get('task_name'),
            description: formData.get('description'),
            priority: formData.get('priority'),
            deadline: formData.get('deadline'),
            status: formData.get('status'),
        };

        fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
            },
            body: JSON.stringify(task_detail_data),
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Failed to create task');
            })
            .then(newTask => {
                createTaskForm.reset();
                createTaskFormContainer.style.display = 'none';
                appendTaskToTable(newTask);
            })
            .catch(error => console.log(error.message));
    });

    updateTaskForm.addEventListener('submit', event => {
        event.preventDefault();

        const formData = new FormData(updateTaskForm);
        const task_id = formData.get('task_id');
        const task_detail_data = {
            task_name: formData.get('task_name'),
            description: formData.get('description'),
            priority: formData.get('priority'),
            deadline: formData.get('deadline'),
            status: formData.get('status'),
        };

        fetch(`${endpoint}${task_id}/`, {
            method: 'PUT',
            headers: {
                'Content-type': 'application/json',
            },
            body: JSON.stringify(task_detail_data),
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Failed to update task');
            })
            .then(updatedTask => {
                const updatedRow = createTaskRow(updatedTask); // Create a new row with updated data
                const existingRow = table.querySelector(`tr[data-task-id="${task_id}"]`);
                existingRow.replaceWith(updatedRow); // Replace old row with updated row

                updateTaskForm.reset();
                updateTaskFormContainer.style.display = 'none';
            })
            .catch(error => console.log(error.message));
    });

    function deleteTask(taskId, rowElement) {
        fetch(`${endpoint}${taskId}/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then(response => {
                if (response.ok) {
                    rowElement.remove();
                } else {
                    throw new Error('Failed to delete task');
                }
            })
            .catch(error => console.log(error.message));
    }

    function appendTaskToTable(task_detail) {
        const rowData = createTaskRow(task_detail);
        table.append(rowData);
    }

    function createTaskRow(task_detail) {
        const rowData = document.createElement('tr');
        rowData.setAttribute('data-task-id', task_detail.id);

        const keys = Object.keys(task_detail);
        keys.forEach(key => {
            if (key !== 'id') {
                const td = document.createElement('td');
                td.textContent = task_detail[key];
                rowData.append(td);
            }
        });

        const deleteCell = document.createElement('td');
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.classList.add('delete-button'); // Add class for identifying delete button

        deleteButton.addEventListener('click', function () {
            const taskId = rowData.getAttribute('data-task-id');
            const taskName = rowData.querySelector('td:first-child').textContent.trim();

            if (confirm(`Are you sure you want to delete "${taskName}"?`)) {
                deleteTask(taskId, rowData);
            }
        });

        deleteCell.append(deleteButton);
        rowData.append(deleteCell);

        const editCell = document.createElement('td');
        const editButton = document.createElement('button');
        editButton.textContent = 'Edit';
        editButton.classList.add('edit-button'); // Add class for identifying edit button

        editButton.addEventListener('click', function () {
            const taskId = rowData.getAttribute('data-task-id');
            const taskName = rowData.querySelector('td:first-child').textContent.trim();

            document.getElementById('update-task-id').value = taskId;
            document.getElementById('update-task-name').value = rowData.querySelector('td:nth-child(1)').textContent.trim();
            document.getElementById('update-description').value = rowData.querySelector('td:nth-child(2)').textContent.trim();
            document.getElementById('update-priority').value = rowData.querySelector('td:nth-child(3)').textContent.trim();
            document.getElementById('update-deadline').value = rowData.querySelector('td:nth-child(4)').textContent.trim();
            document.getElementById('update-status').value = rowData.querySelector('td:nth-child(5)').textContent.trim();

            updateTaskFormContainer.style.display = 'block';
        });

        editCell.append(editButton);
        rowData.append(editCell);

        return rowData;
    }

    table.addEventListener('click', function (event) {
        const target = event.target;

        if (target.classList.contains('edit-button')) {
            // Handle edit button click, if needed
        } else if (target.classList.contains('delete-button')) {
            // Handle delete button click, if needed
        }
    });
});
