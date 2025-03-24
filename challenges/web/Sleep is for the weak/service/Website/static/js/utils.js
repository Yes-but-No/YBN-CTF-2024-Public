async function postRequest(destination,data,action,returnText){
    let formObject = new FormData()
    data = data ?? {} 
    if (!(data instanceof FormData)){
        for (const [key,value] of Object.entries(data)){
            formObject.append(key,value)
        }
    }
    else{
        formObject = data
    }
    
    let response = await fetch(destination, { method: "POST", body: formObject })
    let result
    try{
        if (returnText) result = await response.text()
        else result = await response.json()
    }
    catch (e){
        if (returnText){
            response = await fetch(destination, { method: "POST", body: formObject })
            result = await response.text()
            return result
        }
        return ""
    }
    return action ? action(result) : result 
    
}


async function getRequest(destination,data,action,returnText){
    data = data ?? {} 
    destination += "?"

    if (!(data instanceof FormData)){
        for (const [key,value] of Object.entries(data)){
            destination += `${key}=${value}&`
        }
    }
    else{
        for (const [key,value] of data.entries()){
            destination += `${key}=${value}&`
        }
    }
    response = await fetch(destination, 
        { method: "GET",
        headers: {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }})
    var result
    try{
        if (returnText) result = await response.text()
        else result = await response.json()
    }
    catch (e){
        console.log(e)
        response = await fetch(destination, 
            { method: "GET",
            headers: {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            }})
        result = await response.text()
        console.log(result)
        return result
    }
    
    console.log(result)
    return action ? action(result) : result 
    
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