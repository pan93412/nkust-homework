import {
  Button,
  NativeSelect,
  NumberInput,
  Stack,
  TextInput,
} from "@mantine/core";
import { createFormFactory } from "@tanstack/react-form";
import { zodValidator } from "@tanstack/zod-form-adapter";
import * as zod from "zod";

type FormData = {
  username: string;
  age: number;
  country: "taiwan" | "usa" | "uk";
};

const formFactory = createFormFactory<FormData, typeof zodValidator>({
  defaultValues: {
    username: "",
    age: 0,
    country: "taiwan",
  },
  onSubmit(props) {
    console.log("submit", props.value);
  },
  validatorAdapter: zodValidator,
});

export default function TanstackForm() {
  const form = formFactory.useForm();

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        e.stopPropagation();
        form.handleSubmit();

        console.log("SUBMIT");
      }}
    >
      <Stack>
        <form.Field
          name="username"
          validators={{
            onBlur: zod.string()
              .max(32, "Username must be at most 32 characters")
              .min(3, "Username must be at least 3 characters")
              .regex(/^[a-z0-9_]+$/, "Username must only contain lowercase letters, numbers, and underscores"),
          }}
          children={({ state, handleChange, handleBlur }) => (
            <>
              <TextInput
                label="Username:"
                name="username"
                defaultValue={state.value}
                onChange={(e) => handleChange(e.target.value)}
                onBlur={handleBlur}
                error={state.meta.errors ? state.meta.errors.join(", ") : null}
              />
            </>
          )}
        />

        <form.Field
          name="age"
          validators={{
            onBlur: zod.number()
            .min(18, "You must be at least 18 years old"),
          }}
          children={({ state, handleChange, handleBlur }) => (
            <>
              <NumberInput
                label="Age:"
                name="age"
                error={state.meta.errors ? state.meta.errors.join(", ") : null}
                defaultValue={state.value}
                onChange={(e) => handleChange(Number(e))}
                onBlur={handleBlur}
              />
            </>
          )}
        />

        <form.Field
          name="country"
          validators={{
            onBlur: zod.enum(["taiwan", "usa", "uk"]),
          }}
          children={({ state, handleChange, handleBlur }) => (
            <>
              <NativeSelect
                name="country"
                label="Country or Region:"
                data={[
                  { label: "Taiwan", value: "taiwan" },
                  { label: "USA", value: "usa" },
                  { label: "UK", value: "uk" },
                ]}
                error={state.meta.errors ? state.meta.errors.join(", ") : null}
                defaultValue={state.value}
                onChange={(e) => {
                  switch (e.target.value) {
                    case "taiwan":
                    case "usa":
                    case "uk":
                      handleChange(e.target.value);
                      break;
                    default:
                      break;
                  }
                }}
                onBlur={handleBlur}
              />
            </>
          )}
        />

        <Button type="submit">Submit</Button>
      </Stack>
    </form>
  );
}
