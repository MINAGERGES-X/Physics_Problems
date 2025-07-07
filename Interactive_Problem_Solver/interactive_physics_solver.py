
import math

# this script is dedicated for beginner users of python, where the script include the basic equation used in Kinematics, electricity,

def final_velocity(initial_velocity: float, acceleration: float, time: float) -> float:
    return initial_velocity + acceleration * time

def projectile_motion(angle_deg: float, velocity: float):
    g = 9.81
    angle_rad = math.radians(angle_deg)
    range_ = (velocity**2 * math.sin(2 * angle_rad)) / g
    height = (velocity**2 * (math.sin(angle_rad))**2) / (2 * g)
    return range_, height

def force(mass: float, acceleration: float) -> float:
    return mass * acceleration

def work(force_val: float, distance: float) -> float:
    return force_val * distance

def period(mass: float, spring_constant: float) -> float:
    return 2 * math.pi * math.sqrt(mass / spring_constant)

def electric_field(charge: float, distance: float) -> float:
    k = 8.9875e9
    return k * charge / (distance**2)

def work_done_isothermal(P1: float, V1: float, V2: float) -> float:
    return P1 * V1 * math.log(V2 / V1)

def relativistic_kinetic_energy(mass: float, velocity: float) -> float:
    c = 3e8
    gamma = 1 / math.sqrt(1 - (velocity**2 / c**2))
    return mass * c**2 * (gamma - 1)

def pressure_difference(density: float, height: float) -> float:
    g = 9.81
    return density * g * height

def frequency(speed: float, wavelength: float) -> float:
    return speed / wavelength


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!!")

def main():
    menu = {
        "1": "Kinematics: final velocity (v = u + a t)",
        "2": "Projectile Motion: range & max height",
        "3": "Newton’s Second Law: force (F = m a)",
        "4": "Work & Energy: work done (W = F d)",
        "5": "Simple Harmonic Motion: period (T = 2π√(m/k))",
        "6": "Electricity & Magnetism: electric field (E = k q / r^2)",
        "7": "Thermodynamics: isothermal work (W = P₁V₁ ln(V₂/V₁))",
        "8": "Relativity: kinetic energy (K = mc²(γ − 1))",
        "9": "Fluid Mechanics: pressure difference (ΔP = ρ g h)",
        "10": "Wave Mechanics: frequency (f = v / λ)",
        "0": "Exit"
    }

    print("★ Hello dear Physicist, please select the desired problem ★\n")

    while True:
        print("Select a problem:")
        for key in sorted(menu.keys(), key=lambda x: int(x) if x.isdigit() else -1):
            print(f" {key}. {menu[key]}")
        choice = input("Enter choice (0-10): ").strip()

        if choice == "0":
            print("Invalid selection!!!, Please select for 1 to 10")
            break

        if choice == "1":
            u = get_float("Initial velocity u (m/s): ")
            a = get_float("Acceleration a (m/s²): ")
            t = get_float("Time t (s): ")
            v = final_velocity(u, a, t)
            print(f"→ Final velocity v = {v:.3f} m/s\n")

        elif choice == "2":
            angle = get_float("Launch angle θ (degrees): ")
            v0 = get_float("Initial velocity v₀ (m/s): ")
            r, h = projectile_motion(angle, v0)
            print(f"→ Range = {r:.3f} m, Max height = {h:.3f} m\n")

        elif choice == "3":
            m = get_float("Mass m (kg): ")
            a = get_float("Acceleration a (m/s²): ")
            F = force(m, a)
            print(f"→ Force F = {F:.3f} N\n")

        elif choice == "4":
            F = get_float("Force F (N): ")
            d = get_float("Distance d (m): ")
            W = work(F, d)
            print(f"→ Work W = {W:.3f} J\n")

        elif choice == "5":
            m = get_float("Mass m (kg): ")
            k = get_float("Spring constant k (N/m): ")
            T = period(m, k)
            print(f"→ Period T = {T:.3f} s\n")

        elif choice == "6":
            q = get_float("Charge q (C): ")
            r = get_float("Distance r (m): ")
            E = electric_field(q, r)
            print(f"→ Electric field E = {E:.3e} N/C\n")

        elif choice == "7":
            P1 = get_float("Initial pressure P₁ (Pa): ")
            V1 = get_float("Initial volume V₁ (m³): ")
            V2 = get_float("Final volume V₂ (m³): ")
            W = work_done_isothermal(P1, V1, V2)
            print(f"→ Work done W = {W:.3f} J\n")

        elif choice == "8":
            m = get_float("Mass m (kg): ")
            v = get_float("Velocity v (m/s): ")
            K = relativistic_kinetic_energy(m, v)
            print(f"→ Relativistic KE K = {K:.3e} J\n")

        elif choice == "9":
            rho = get_float("Density ρ (kg/m³): ")
            h = get_float("Height h (m): ")
            dP = pressure_difference(rho, h)
            print(f"→ Pressure difference ΔP = {dP:.3f} Pa\n")

        elif choice == "10":
            v = get_float("Wave speed v (m/s): ")
            lam = get_float("Wavelength λ (m): ")
            f = frequency(v, lam)
            print(f"→ Frequency f = {f:.3f} Hz\n")

        else:
            print("Invalid selection. Please choose a number from 0 to 10.\n")

if __name__ == "__main__":
    main()
