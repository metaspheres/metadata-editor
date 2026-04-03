document.getElementById("folder-browser-input").addEventListener("input", getPath)

function getPath(event){
    const path = event.target.value
    fetch('/browse?path=' + path)
    .then(response => response.json())
    .then(data => {

        const suggestions = document.getElementById("suggestions")
        suggestions.innerHTML = ""
        data.forEach(path =>{
            console.log("Creating item for:", path)
            const item = document.createElement("div")
            item.textContent = path
            item.addEventListener("click", () => {
                document.getElementById("folder-browser-input").value = path
                document.getElementById("selected-path").value = path       
                getPath()

            })
            suggestions.appendChild(item)
        })

    })
}

document.querySelector("form").addEventListener("submit", () => {
    const typedPath = document.getElementById("folder-browser-input").value
    const hiddenInput = document.getElementById("selected-path")
    if (!hiddenInput.value) {
        hiddenInput.value = typedPath
    }
})


                  