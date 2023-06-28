import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import max_error, mean_absolute_error


class Machine:

    def __init__(self):
        pass

    def score_machine(self, data):
        np.random.seed(89)

        x = data.drop(["Rating"], axis=1)
        y = data["Rating"]

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=89)

        model = RandomForestRegressor(n_estimators=260, max_samples=61, min_samples_split=3,
                                      min_samples_leaf=3, min_impurity_decrease=4)

        model.fit(x_train, y_train)

        r_score = model.score(x_test, y_test)

        y_preds = model.predict(x_test)
        m_error = max_error(y_test, y_preds)
        m_a_error = mean_absolute_error(y_test, y_preds)

        scores = ['R squared: %.2f' % r_score, 'Maximum Residual Error: %.2f' % m_error,
                  'Mean Absolute Error: %.2f' % m_a_error]

        return scores

    def get_machine(self, data):
        np.random.seed(42)

        x = data.drop(["Rating"], axis=1)
        y = data["Rating"]

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.15, random_state=42)

        model = RandomForestRegressor(n_estimators=220, max_samples=43, min_samples_split=10,
                                      min_samples_leaf=3, min_impurity_decrease=6)

        model.fit(x_train, y_train)
        return model

    def predict(self, model, x):
        rating = model.predict(x)
        return rating
