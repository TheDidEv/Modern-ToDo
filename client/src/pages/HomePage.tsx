import useAuthStore from "../context/AuthStore";


const HomePage = () => {
    const { refresh_token } = useAuthStore();

    return (
        <div>
            <div>HomePage</div>
            <p>{refresh_token}</p>
        </div>
    )
}

export default HomePage;