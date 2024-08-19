import { useEffect, useState } from "react";
import useAuthStore from "../context/AuthStore";
import { redirect } from "react-router-dom";

const LoginPage = () => {
    const { isAuthenticated, login, error } = useAuthStore();

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    useEffect(() => {
        if (isAuthenticated) {
            redirect('/');
        }
    })

    const handlerSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        await login(username, password);
    }

    return (
        <div>
            <div>
                <form onSubmit={handlerSubmit}>
                    <input
                        onChange={e => setUsername(e.target.value)}
                        value={username}
                        type="username"
                        placeholder="username"
                    />

                    <input
                        onChange={e => setPassword(e.target.value)}
                        value={password}
                        type="password"
                        placeholder="password"
                    />
                </form>

                <button
                    onClick={handlerSubmit}
                >
                    Login
                </button>
                {error && <p>{error}</p>}
            </div>
        </div>
    );
}

export default LoginPage;