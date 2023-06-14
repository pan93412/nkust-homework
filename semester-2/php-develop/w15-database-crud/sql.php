<?php

namespace Client;
require_once 'config.php';

use PDO;

class CustomPdo extends PDO
{
    private \PDOStatement $retrieveStatement;
    private \PDOStatement $createStatement;

    public function __construct()
    {
        $host = MYSQL_HOST;
        $name = MYSQL_NAME;
        $charset = MYSQL_CHARSET;
        $user = MYSQL_USER;
        $password = MYSQL_PASSWORD;

        $dsn = "mysql:host=$host;dbname=$name;charset=$charset";

        parent::__construct($dsn, $user, $password, [PDO::ERRMODE_EXCEPTION]);

        $this->retrieveStatement = $this->prepare("SELECT * FROM `student`");
        $this->createStatement = $this->prepare("INSERT INTO `student` (`id`, `name`, `birth`, `addr`) VALUES (:id, :name, :birth, :addr)");
    }

    /**
     * @return array<StudentSchema>
     */
    public function retrieveAllRows(): array
    {
            $this->retrieveStatement->execute();
            return $this->retrieveStatement->fetchAll(PDO::FETCH_ASSOC);
    }

    /**
     * Create a student record.
     *
     * @param string $id
     * @param string $name
     * @param string $birth
     * @param string $addr
     * @return void
     */
    public function createStudent(string $id, string $name, string $birth, string $addr): void
    {
        $this->createStatement->execute([
            'id'       => $id,
            'name'     => $name,
            'birth'    => $birth,
            'addr'     => $addr,
        ]);
    }
}

class StudentSchema {
    public string $id;
    public string $name;
    public string $birth;
    public string $addr;
}
