import { Route, Routes } from 'react-router-dom';
import './App.css';

import PrivateRoute from './utils/PrivateRoute';

import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import Header from './components/Header';
import AuthStore from './context/AuthStore';

function App() {
  // const isAuthenticated: boolean = true;
  const { isAuthenticated } = AuthStore();

  return (
    <div className="App">

      <Routes>

        <Route element={<LoginPage />} path="/login" />
        <Route element={<PrivateRoute isAuthenticated={isAuthenticated} />}>
          <Route element={<HomePage />} path="/" />
        </Route>

      </Routes>
    </div >
  );
}

export default App;
