import NavItem from "./NavItem";
import Sound from "./Sound";

export default function Nav() {
    return (
      <nav className="fixed top-0 left-0 w-full bg-blue-600/50 text-white shadow-md flex items-center justify-between px-6 py-3 z-10">
            <div className="flex items-center">
                <Sound />
            </div>

            <div className="flex gap-6">
                <NavItem link="/">Home</NavItem>
                <NavItem link="/shop">Shop</NavItem>
                <NavItem link="/signup">Signup</NavItem>
                <NavItem link="/login">Login</NavItem>
            </div>
        </nav>
    );
}
