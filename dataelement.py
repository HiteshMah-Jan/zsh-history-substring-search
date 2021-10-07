const SALARY_TYPE_FULL = 0;
    const SALARY_TYPE_HOUR = 1;

    public function __construct(Salary $model)
    {
        $this->model = $model;
    }
 })
            ->addColumn('salary', function($candidate) {
                return @format_price($candidate->user_preferences->salary);
            })
            ->addColumn('contract_type', function($candidate) {
