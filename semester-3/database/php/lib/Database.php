<?php

require_once __DIR__ . "/Student.php";
require_once __DIR__ . "/Model.php";
require_once __DIR__ . "/Meta.php";


final class Database extends mysqli {
    public function __construct(public string $database = "myschool")
    {
        parent::__construct(
            "db",
            "db",
            "db",
            $database,
            3306,
        );
    }

    public function info(): array
    {
        return [
           "主機資訊" => $this->host_info,
           "伺服器資訊" => $this->server_info,
           "通訊協定版本" => $this->protocol_version,
           "客戶端函式庫資訊" => $this->client_info,
        ];
    }

    /**
     * @return array<Student>
     * @throws ReflectionException
     */
    public function listAll(string $class): array
    {
        $tableName = $this->getTableName($class);
        $result = $this->query("SELECT * FROM ".$tableName);

        $rows = [];
        while ($row = $result->fetch_object($class)) {
            $rows[] = $row;
        }

        $result->close();
        return $rows;
    }

    /**
     * @throws ReflectionException
     */
    private function getTableName(string $class): string {
        $r = new \ReflectionClass($class);

        /** @var Model $c */
        $c = $r->newInstanceWithoutConstructor();
        return $c->tableName();
    }

    /**
     * @param array $values
     * @return array<string>
     */
    private function getParamType(array $values): string
    {
        $types = [];
        foreach ($values as $value) {
            if (is_int($value)) {
                $types[] = "i";
            } else if (is_float($value)) {
                $types[] = "d";
            } else {
                $types[] = "s";
            }
        }
        return join("", $types);
    }

    public function insert(ModelRequestDto $dto): bool {
        $tableName = $dto->tableName();
        $entity = $dto->nonNullEntries();

        $keys = array_keys($entity);
        $valuesPlaceholder = implode(",", array_fill(0, count($entity), "?"));
        $values = array_values($entity);

        $sql = "INSERT INTO ".$tableName." (".implode(",", $keys).") VALUES (".$valuesPlaceholder.")";
        $stmt = $this->prepare($sql);
        $stmt->bind_param($this->getParamType($values), ...$values);

        return $stmt->execute();
    }

    /**
     * @throws ReflectionException
     */
    public function getMetadata(string $class): Meta|null
    {
        $tableName = $this->getTableName($class);
        $result = $this->query("SELECT * FROM ".$tableName);
        if (!$result) return null;

        $meta = new Meta($class, $result);
        $result->close();

        return $meta;
    }

    /**
     * @throws ReflectionException
     */
    public function getEntriesByPage(string $class, int $page, int $limit): array
    {
        $tableName = $this->getTableName($class);
        $result = $this->query("SELECT * FROM ".$tableName);
        $result->data_seek(($page - 1) * $limit);

        $rows = [];
        for ($i = 0; $i < $limit; $i++) {
            $row = $result->fetch_object($class);
            if (!$row) break;
            $rows[] = $row;
        }

        $result->close();
        return $rows;
    }

    public function __destruct()
    {
        $this->close();
    }
}