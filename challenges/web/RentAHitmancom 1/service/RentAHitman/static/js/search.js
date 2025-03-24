async function postRequest(destination, data) {
    let formObject = new FormData()
    data = data ?? {}
    if (data instanceof FormData) formObject = data
    else {
        for (const [key, value] of Object.entries(data)) {
            formObject.append(key, value)
        }
    }
    let response = await fetch(destination, { method: "POST", body: formObject })
    let result
    try {
        result = await response.json()
    }
    catch (e) {
        alert(e)
        return "Failure"
    }
    return result

}
function createEle(eleTag,classList,id,attributes,styles){

    const ele = document.createElement(eleTag)
    classList = classList ?? []
    classList = typeof classList == "string" ? [classList]:classList 
    attributes = attributes ?? {}
    styles = styles ?? {}
    for (var className of classList){
        ele.classList.add(className)
    }
    for (var [attrName,attrVal] of Object.entries(attributes)){
        ele[attrName] = attrVal
    }
    for (var [styleName,styleVal] of Object.entries(styles)){
        ele.style[styleName] = styleVal
    }
    if (id) ele.id = id 
    return ele
}
function createCard(name, location, description) {
    const card = createEle('div', [
        'bg-white', 
        'shadow-md', 
        'rounded-xl', 
        'w-1/4', 
        'text-lg', 
        'px-6', 
        'py-4', 
        'hover:shadow-lg', 
        'hover:scale-105', 
        'transition-all', 
        'border', 
        'border-gray-200'
    ]);

    const title = createEle('h3', ['font-bold', 'text-2xl', 'text-gray-800', 'mb-2'], null, {
        innerText: name
    });

    const locationEle = createEle('p', ['text-base', 'text-gray-600', 'mb-1'], null, {
        innerText: `📍 Location: ${location}`
    });

    const descriptionEle = createEle('p', ['text-base', 'text-gray-600'], null, {
        innerText: `📝 Description: ${description}`
    });

    card.appendChild(title);
    card.appendChild(locationEle);
    card.appendChild(descriptionEle);

    return card;
}

const input = document.querySelector('input')
const targetContainer = document.querySelector('#targets')
var search = input.value
setInterval(async ()=>{    
    if (search == input.value) return
    search = input.value;
    const data = { search: search }
    const result = await postRequest('/filter', data)
    targetContainer.innerHTML = ""
    for (const row of result){
        const card = createCard(row[0], row[1], row[2])
        targetContainer.appendChild(card)
    }
},5000);