package org.jboss.training.was.impl;

import javax.ejb.EJB;
import org.assertj.core.api.Assertions;
import org.jboss.arquillian.container.test.api.OperateOnDeployment;
import org.jboss.training.was.api.Calculator;
import org.junit.Test;

public class CalculatorImplTest extends ArquillianTest {

    @EJB
    private Calculator<Integer> calculator;

    @OperateOnDeployment(ArquillianTest.DEPLOYMENT_MANAGED)
    @Test
    public void testAddition() {
        int result = calculator.add(3, 7);
        Assertions.assertThat(result).isEqualTo(10);
    }
}
