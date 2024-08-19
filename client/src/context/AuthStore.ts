import { create } from "zustand";
import { loginApi, UserData } from "../api/AuthApi";

interface AuthState {
    isAuthenticated: boolean,
    user: UserData | null,
    refresh_token: string | null,
    access_token: string | null,
    error: string | null,
    login: (username: string, password: string) => Promise<void>
}

const useAuthStore = create<AuthState>((set, get) => ({
    isAuthenticated: false,
    user: null,
    refresh_token: null,
    access_token: null,
    error: null,

    login: async (username, password) => {
        try {
            const data = await loginApi(username, password);

            const typeData = data as { user: UserData, access: string, refresh: string };
            // if (typeData.access !== null && typeData.refresh !== null) {
                localStorage.setItem("access", typeData.access);
                console.log("DATA:", typeData);
                set({
                    isAuthenticated: true,
                    // user: typeData.user,
                    access_token: typeData.access,
                    refresh_token: typeData.refresh,
                    error: null,
                });
            // }
            // set({ isAuthenticated: false });

        } catch (error: any) {
            console.error("Login error", error);

            set({
                isAuthenticated: false,
                error: error.message || "Login failed. Please check your credentials."
            });
        }
    }
}));

export default useAuthStore;