document.getElementById("folder-browser-input").addEventListener("input", getPath)

function getPath(event){
    const path = event.target.value
    fetch('/browse?path=' + path)
    .then(response => response.json())
    .then(data => {

        const suggestions = document.getElementById("suggestions")
        suggestions.innerHTML = ""
        data.forEach(path =>{
            const item = document.createElement("div")
            item.textContent = path
            item.addEventListener("click", () => {
                document.getElementById("folder=browser=input").value = path
                getPath()
            })
            suggestions.appendChild(item)
        })

    })
}

