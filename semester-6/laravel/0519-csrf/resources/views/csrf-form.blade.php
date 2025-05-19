<form action="{{ route('csrf-form.store') }}" method="POST">
    @csrf

    <label for="csrfform__name">Your name:</label>
    <input type="text" name="name" id="csrfform__name">

    <button type="submit">Submit</button>
</form>
