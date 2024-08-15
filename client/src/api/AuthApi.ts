import AxiosInstance from "../utils/AxiosInstance";

export interface UserData {
    username: string,
    email: string,
}

export const loginApi = async (username: string, password: string) => {
    const response = await AxiosInstance.post(`/api/token`, { username, password });
    return response.data;
}