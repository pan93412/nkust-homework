import styled from "@emotion/styled";

export const IntroCard = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

export const Avatar = styled.img`
  width: 150px;
  height: 150px;
  border-radius: 50%;
`;

export const Title = styled.h1`
  font-size: 1.5em;
  margin: 0.5em;
`;

export const Button = styled("button")`
  background-color: transparent;
  color: darkgray;
  border: 1px solid darkgray;
  border-radius: 0.25em;
`;

export const PositiveButton = styled(Button)`
  color: darkblue;
`;

export const NegativeButton = styled.button`
  ${Button}
  color: darkred;
`;
