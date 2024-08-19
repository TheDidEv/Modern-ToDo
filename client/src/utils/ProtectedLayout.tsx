import { Navigate, Outlet } from "react-router-dom";
import useAuthStore from "../context/AuthStore";

export const ProtectedLayout = () => {
    const { isAuthenticated } = useAuthStore();

    if (!isAuthenticated) {
        return <Navigate replace to={'/login'} />;
    }

    return (
        <>
            <Outlet />
        </>
    )
}

export default ProtectedLayout;