let addToDoButton = document.getElementById('addToDo');
let toDoContainer = document.getElementById('toDoContainer');
let inputField = document.getElementById('inputField');

addToDoButton.addEventListener('click', function(){
    var paragraph = document.createElement('p');
    paragraph.classList.add('paragraph-styling');
    paragraph.innerText = inputField.value;

    var deleteButton = document.createElement('button');
    deleteButton.innerText = 'Delete';
    deleteButton.classList.add('delete-button');

    paragraph.appendChild(deleteButton);
    toDoContainer.appendChild(paragraph);
    inputField.value = "";

    deleteButton.addEventListener('click', function(){
        toDoContainer.removeChild(paragraph);
    });

    paragraph.addEventListener('click', function(){
        paragraph.style.textDecoration = "line-through";
    });
});
