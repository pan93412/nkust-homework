import { Form } from '@remix-run/react';
import { ActionFunctionArgs, redirect } from '@remix-run/node';

// Mock handler for form submission
export async function action({ request }: ActionFunctionArgs) {
  console.log(await request.text());

  // Redirect to a thank you page or simply return success message
  return redirect("/thank-you");
}

export default function ExtendedTypesForm() {
    return (
      <div>
        <h1>Extended Types Form</h1>
        <Form method="post">
          <label>
            Text:
            <input type="text" name="textInput" required />
          </label>
          <br />

          <label>
            Email:
            <input type="email" name="emailInput" placeholder="@gmail.com" />
          </label>
          <br />

          <label>
            Password:
            <input type="password" name="passwordInput" />
          </label>
          <br />

          <label>
            Number:
            <input type="number" name="numberInput" />
          </label>
          <br />

          <label>
            Date:
            <input type="date" name="dateInput" />
          </label>
          <br />

          <label>
            Datetime-Local:
            <input type="datetime-local" name="datetimeInput" />
          </label>
          <br />

          <label>
            Color:
            <input type="color" name="colorInput" />
          </label>
          <br />

          <label>
            Search:
            <input type="search" name="searchInput" />
          </label>
          <br />

          <label>
            Telephone:
            <input type="tel" name="telInput" />
          </label>
          <br />

          <label>
            Range:
            <input type="range" name="rangeInput" min="0" max="100" />
          </label>
          <br />

          <fieldset>
            <legend>Radio:</legend>
            <label>
              Option 1
              <input type="radio" name="radioInput" value="option1" />
            </label>
            <label>
              Option 2
              <input type="radio" name="radioInput" value="option2" />
            </label>
          </fieldset>
          <br />

          <label>
            Checkbox:
            <input type="checkbox" name="checkboxInput" value="check1" />
            Check 1
          </label>
          <br />

          <label>
            Select Dropdown:
            <select name="selectInput">
              <option value="option1">Option 1</option>
              <option value="option2">Option 2</option>
            </select>
          </label>
          <br />

          <label>
            Textarea:
            <textarea name="textareaInput" rows={4}></textarea>
          </label>
          <br />

          <button type="submit">Submit</button>
        </Form>
      </div>
    );
  }
