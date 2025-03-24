async function getRequest(url: string, data?: object, options?: RequestInit) {
    let response
    try {
        let finalUrl = url;
        if (data && typeof data === 'object') {
            const queryParams = new URLSearchParams(data as Record<string, string>).toString();
            finalUrl += '?' + queryParams;
        }

        response = await fetch(finalUrl, {
            method: 'GET',
            ...options,
        });

        

        
    } catch (error) {
        console.error(error);
    }
    const json = await response?.json();
    if (!response?.ok && !json?.error) {
        json.error = 'An Unknown Error occurred';
    }
    return json;
}

async function postRequest(url: string, data: object | FormData, options?: RequestInit) {
    let response 
    try {
        // Convert FormData to a plain object if 'data' is FormData
        let jsonData: Record<string, any>;

        if (data instanceof FormData) {
            jsonData = {}; // Initialize jsonData with an appropriate type
            data.forEach((value: any, key: string) => {
            jsonData[key] = value;
            });
        } else {
            jsonData = data;
        }

        const headers = {
            'Content-Type': 'application/json',
            ...options?.headers,
        };

        const body = JSON.stringify(jsonData);

        response = await fetch(url, {
            method: 'POST',
            headers,
            body,
            ...options,
        });


    } catch (error) {
        console.error(error);
    }
    const json = await response?.json();
    if (!response?.ok && !json?.error) {
        json.error = 'An Unknown Error occurred';
    }
    return json;

}




export { getRequest, postRequest };