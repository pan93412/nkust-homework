import Coupon from "~/components/Coupon";
import {createSignal, For} from "solid-js";

const coupons = [
	{
		name: "50% off",
		description: "Get 50% off your first purchase!",
	},
	{
		name: "Free shipping",
		description: "Free shipping on orders over $50",
	},
	{
		name: "10% off",
		description: "Get 10% off your next purchase!",
	},
	{
		name: "20% off",
		description: "Get 20% off your next purchase!",
	},
	{
		name: "Buy 1, get 1 free",
		description: "Buy 1, get 1 free on the entire store!",
	},
	{
		name: "30% off",
		description: "Get 30% off your next purchase!",
	},
];
export default function Home() {
	const [selectedCoupon, setSelectedCoupon] = createSignal<string | null>(null);

	return (
		<main class="m-16 space-y-16">
			<h1 class={"text-2xl text-center"}>You are selecting the coupon “{selectedCoupon()}”</h1>
			<section class="grid grid-cols-3 gap-8">
				<For each={coupons}>
					{(coupon) => {
						return <Coupon name={coupon.name} onSelected={setSelectedCoupon}>
							<p>{coupon.description}</p>
						</Coupon>;
					}}
				</For>
			</section>
		</main>
	);
}
