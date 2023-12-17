<?php

require_once __DIR__ . "/Model.php";

class Student extends Model {
    public string $sno;
    public string $name;
    public string $address;
    public string $birthday;
    public string $username;
    public string $password;

    public static function tableName(): string
    {
        return "students";
    }

    /**
     * @return string[]
     */
    public static function header(): array {
        return [
            "學號",
            "姓名",
            "地址",
            "生日",
            "帳號",
            "密碼",
        ];
    }

    public function toArray(): array
    {
        return [
            $this->sno,
            $this->name,
            $this->address,
            $this->birthday,
            $this->username,
            $this->password,
        ];
    }
}