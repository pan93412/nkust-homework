<?php

namespace Client;

use PDO;

class CustomPdo extends PDO
{
    private \PDOStatement $createStatement;

    public function __construct()
    {
        $host = "localhost";
        $name = "panclient_school";
        $user = "panclient";
        $password = "";
        $charset = "utf8mb4";

        $dsn = "mysql:host=$host;dbname=$name;charset=$charset";

        parent::__construct($dsn, $user, $password);

        $this->createStatement = $this->prepare("SELECT * FROM `student`");
    }

    /**
     * @return array<StudentSchema>
     */
    public function retrieveAllRows(): array
    {
            $this->createStatement->execute();
            return $this->createStatement->fetchAll(PDO::FETCH_ASSOC);
    }
}

class StudentSchema {
    public string $id;
    public string $name;
    public string $birth;
    public string $addr;
}
