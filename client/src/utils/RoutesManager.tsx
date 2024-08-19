import { Route, Routes, useLocation } from 'react-router-dom';

import HomePage from "./../pages/HomePage";
import LoginPage from "./../pages/LoginPage";
import Header from './../components/Header';
import DefaultLayout from './../utils/DefaultLayout';
import ProtectedLayout from './../utils/ProtectedLayout';

const RoutesManager = () => {
    const location = useLocation().pathname;

    return (
        <>
            {location !== '/login' && location !== '/register' && <Header />}

            <Routes>
                <Route element={<DefaultLayout />}>
                    <Route path='/login' element={<LoginPage />} />
                </Route>

                <Route element={<ProtectedLayout />}>
                    <Route index element={<HomePage />} />
                </Route>
            </Routes>
        </>
    );
}

export default RoutesManager;
