<?php

require_once __DIR__ . "/Model.php";

class Contact extends Model
{
    public int $id;
    public string $name;
    public string $tel;


    public static function tableName(): string
    {
        return "contact";
    }

    public static function header(): array
    {
        return ["ID", "名字", "聯絡方式"];
    }

    public function toArray(): array
    {
        return [strval($this->id), $this->name, $this->tel];
    }
}

class ContactModelRequestDto extends ModelRequestDto {
    public ?string $id;
    public string $name;
    public string $tel;

    public function __construct(array $postData)
    {
        $this->id = $postData["id"] ?? null;
        $this->name = $postData["name"];
        $this->tel = $postData["tel"];
    }

    public static function tableName(): string
    {
        return "contact";
    }
}
