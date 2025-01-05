import React from "react";
import { ScrollView } from "react-native";
import { PricingCard, lightColors } from "@rneui/themed";

export default function PricingView() {
    return (
        <ScrollView>
            <PricingCard
                color={lightColors.primary}
                title="免費"
                price="$0"
                info={["1 位使用者", "基本支援", "所有核心功能"]}
                button={{ title: " 開始使用", icon: "flight-takeoff" }}
            />
            <PricingCard
                color={lightColors.secondary}
                title="入門"
                price="$19"
                info={["10 位使用者", "基本支援", "所有核心功能"]}
                button={{ title: " 開始使用", icon: "flight-takeoff" }}
            />
            <PricingCard
                color={lightColors.success}
                title="企業"
                price="$49"
                info={["100 位使用者", "一對一支援", "所有核心功能"]}
                button={{ title: " 開始使用", icon: "flight-takeoff" }}
            />
        </ScrollView>
    );
}
