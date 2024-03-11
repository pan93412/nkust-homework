import type { JSX } from "solid-js";

export interface CouponProps {
	name: string;
	children: JSX.Element;
	onSelected: (couponName: string) => void;
}

export default function Coupon({ name, children, onSelected }: CouponProps) {
	return (
		<div class="flex flex-col">
			<button
				class="
					group
				bg-neutral-100
					border shadow rounded text-left
					px-6 py-4 w-full min-h-36 overflow-hidden
					flex flex-col justify-between gap-2
					transition transition-200 hover:transform hover:scale-110
				"
				type="button"
				onClick={() => onSelected(name)}
			>
				<div class="space-y-2">
					<h2 class="text-neutral-800 text-xl font-bold">{name}</h2>
					<div class={"text-neutral-900"}>{children}</div>
				</div>
				<div class={"transition transition-200 transform group-hover:translate-y-0 translate-y-20"}>
					<div class="text-neutral-400 text-sm mt-4">Click to enable this coupon →</div>
				</div>
			</button>
		</div>
	);
}
