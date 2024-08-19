import { Navigate, Outlet } from "react-router-dom";
import useAuthStore from "../context/AuthStore";

export const DefaultLayout = () => {
    const { isAuthenticated } = useAuthStore();

    if (isAuthenticated) {
        return <Navigate to={'/'} />;
    }

    return (
        <>
            <Outlet />
        </>
    )
}

export default DefaultLayout;