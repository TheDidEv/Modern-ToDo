export interface UserData {
    username: string,
    email: string,
}

export const loginApi = async (username: string, password: string) => {
    let response = await fetch('http://127.0.0.1:8000/api/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'username': username, 'password': password })
    })
    let data = await response.json()

    return data;
}