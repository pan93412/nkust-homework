import type { Height, Weight } from "./bmi.js";

type OptionalNode = Node | null | undefined;

type TextLabelProps = {
  name: string;
  type?: string;
  placeholder?: string;
};

function TextLabel(
  { name, type, placeholder }: TextLabelProps,
  ...nodes: OptionalNode[]
) {
  const label = document.createElement("label");
  label.innerText = `${name}：`;

  const input = document.createElement("input");
  if (type) input.type = type;
  if (placeholder) input.placeholder = placeholder;

  label.appendChild(input);

  for (const node of nodes) {
    if (node) label.appendChild(node);
  }

  return [label, input] as const;
}

type TextBlockProps = {
  labelBlock: ReturnType<typeof TextLabel>[0];
};

function TextBlock({ labelBlock }: TextBlockProps, ...nodes: OptionalNode[]) {
  const div = document.createElement("div");

  div.appendChild(labelBlock);

  for (const node of nodes) {
    if (node) div.appendChild(node);
  }

  return div;
}

function Bmi() {
  const bmi = document.createElement("div");
  bmi.innerText = "BMI:";
  const bmiContent = document.createElement("span");
  bmi.appendChild(bmiContent);

  return [bmi, bmiContent];
}

export default function App() {
  const app = document.createElement("div");

  const [heightLabel, heightInput] = TextLabel({
    name: "身高",
    type: "number",
    placeholder: "請輸入身高",
  });
  heightLabel.append("公分");
  const [weightLabel, weightInput] = TextLabel({
    name: "體重",
    type: "number",
    placeholder: "請輸入體重",
  });
  weightLabel.append("公斤");

  const heightBlock = TextBlock({ labelBlock: heightLabel });
  const weightBlock = TextBlock({ labelBlock: weightLabel });

  const [bmi, bmiContent] = Bmi();

  const button = document.createElement("button");
  button.innerText = "計算";
  button.onclick = async function () {
    const { calculateBmi, renderBmi } = await import("./bmi.js");

    const bmi = calculateBmi(
        +heightInput.value as Height,
        +weightInput.value as Weight,
    );

    bmiContent.innerText = renderBmi(bmi);
  };

  app.appendChild(heightBlock);
  app.appendChild(weightBlock);
  app.appendChild(bmi);
  app.appendChild(button);

  return app;
}
