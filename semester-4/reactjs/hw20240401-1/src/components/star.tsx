import styled from '@emotion/styled';
import type { Signal } from '@preact/signals';
import { FaStar } from 'react-icons/fa';

const ActiveStar = () => <FaStar color="gold" />;
const InactiveStar = () => <FaStar color="black" />;
const StarButton = styled.button`
    background-color: transparent;
    border: none;
    padding: 0.25em;
`;

export interface StarIdentifierProps {
    activeStar: Signal<number>;
    totalStar?: number;
    onSelectedStar: (star: number) => void;
}

export function StarIdentifier({activeStar, totalStar = 5, onSelectedStar}: StarIdentifierProps) {
    if (activeStar.value > totalStar) {
        throw new Error("activeStar should not be greater than totalStar");
    }

    return (
        <div>
            {new Array(totalStar).fill(null).map((_, idx) => {
                const star = idx+1;
                const isActive = star <= activeStar.value;
                return (
                    <StarButton type="button" key={star} onClick={() => onSelectedStar(star)}>
                        {isActive ? <ActiveStar /> : <InactiveStar />}
                    </StarButton>
                );
            })}
        </div>
    );
}
