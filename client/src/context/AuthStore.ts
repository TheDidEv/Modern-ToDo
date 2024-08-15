import { create } from "zustand";
import { loginApi, UserData } from "../api/AuthApi";

interface AuthState {
    isAuthenticated: boolean,
    user: UserData | null,
    refresh_token: string | null,
    access_token: string | null,
    login: (username: string, password: string) => Promise<void>
}

const AuthStore = create<AuthState>((set, get) => ({
    isAuthenticated: false,
    user: null,
    refresh_token: null,
    access_token: null,

    login: async (username, password) => {
        try {
            const data = await loginApi(username, password);
            // set({ isAuthenticated: true, user: data.user, access_token: data.access, refresh_token: data.refresh_token });
        } catch (error) {
            console.error("Login error", error);
        }
    }
}));

export default AuthStore;