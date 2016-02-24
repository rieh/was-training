package org.jboss.training.was.impl;

import javax.ejb.Stateless;
import org.jboss.training.was.api.Calculator;

@Stateless
public class CalculatorImpl implements Calculator<Integer> {

    public Integer add(final Integer x, final Integer y) {
        return x + y;
    }

    public Integer sub(final Integer x, final Integer y) {
        return x - y;
    }

    public Integer div(final Integer x, final Integer y) {
        return x / y;
    }

    public Integer mult(final Integer x, final Integer y) {
        return x * y;
    }
}
